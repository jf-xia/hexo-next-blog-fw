---
title: "*实战理解 DI & IoC 设计模式"
date: 2017-03-10 08:00:00
updated: 2017-03-15 09:14:34
tags: ["开发"]
---

**摘要: **理解什么是Di/IoC，依赖注入/控制反转。两者说的是一个东西，是当下流行的一种设计模式。大致的意思就是，准备一个盒子(容器)，事先将项目中可能用到的类扔进去，在项目中直接从容器中拿，也就是避免了直接在项目中到处new，造成大量耦合。取而代之的是在项目类里面增设 setDi()和getDi()方法，通过Di同一管理类。 
详细概念推荐文章： <http://docs.phalconphp.com/en/latest/reference/di.html>
中文版： <http://phalcon.5iunix.net/reference/di.html>
 
```php
<?php
class Di implements \ArrayAccess{
    private $_bindings = array();//服务列表
    private $_instances = array();//已经实例化的服务
    
    //获取服务
    public function get($name,$params=array()){
        //先从已经实例化的列表中查找
        if(isset($this->_instances[$name])){
            return $this->_instances[$name];
        }
        
        //检测有没有注册该服务
        if(!isset($this->_bindings[$name])){
            return null;
        }
        
        $concrete = $this->_bindings[$name]['class'];//对象具体注册内容
        
        $obj = null;
        //匿名函数方式
        if($concrete instanceof \Closure){
            $obj = call_user_func_array($concrete,$params);
        }
        //字符串方式
        elseif(is_string($concrete)){
            if(empty($params)){
                $obj = new $concrete;
            }else{
                //带参数的类实例化，使用反射
                $class = new \ReflectionClass($concrete);
                $obj = $class->newInstanceArgs($params);
            }
        }
        //如果是共享服务，则写入_instances列表，下次直接取回
        if($this->_bindings[$name]['shared'] == true && $obj){
            $this->_instances[$name] = $obj;
        }
        
        return $obj;
    }
    
    //检测是否已经绑定
    public function has($name){
        return isset($this->_bindings[$name]) or isset($this->_instances[$name]);
    }
    
    //卸载服务
    public function remove($name){
        unset($this->_bindings[$name],$this->_instances[$name]);
    }
    
    //设置服务
    public function set($name,$class){
        $this->_registerService($name, $class);
    }
    
    //设置共享服务
    public function setShared($name,$class){
        $this->_registerService($name, $class, true);
    }
    
    //注册服务
    private function _registerService($name,$class,$shared=false){
        $this->remove($name);
        if(!($class instanceof \Closure) && is_object($class)){
            $this->_instances[$name] = $class;
        }else{
            $this->_bindings[$name] = array("class"=>$class,"shared"=>$shared);
        }
    }
    
    //ArrayAccess接口,检测服务是否存在
    public function offsetExists($offset) {
        return $this->has($offset);
    }
    
    //ArrayAccess接口,以$di[$name]方式获取服务
    public function offsetGet($offset) {
        return $this->get($offset);
    }
    
    //ArrayAccess接口,以$di[$name]=$value方式注册服务，非共享
    public function offsetSet($offset, $value) {
        return $this->set($offset,$value);
    }
    
    //ArrayAccess接口,以unset($di[$name])方式卸载服务
    public function offsetUnset($offset) {
        return $this->remove($offset);
    }
}
```

演示：

```php
<?php

header("Content-Type:text/html;charset=utf8");
class A{
    public $name;
    public $age;
    public function __construct($name=""){
        $this->name = $name;
    }
}

include "di.php";
$di = new Di();
//匿名函数方式注册一个名为a1的服务
$di->setShared('a1',function($name=""){
    return new A($name);
});
//直接以类名方式注册
$di->set('a2','A');
//直接传入实例化的对象
$di->set('a3',new A("小唐"));

$a1 = $di->get('a1',array("小李"));
echo $a1->name."<br/>";//小李
$a1_1 = $di->get('a1',array("小王"));
echo $a1->name."<br/>";//小李
echo $a1_1->name."<br/>";//小李

$a2 = $di->get('a2',array("小张"));
echo $a2->name."<br/>";//小张
$a2_1 = $di->get('a2',array("小徐"));
echo $a2->name."<br/>";//小张
echo $a2_1->name."<br/>";//小徐

$a3 = $di['a3'];//可以直接通过数组方式获取服务对象
echo $a3->name."<br/>";//小唐


//error_reporting(0);

//class Container
//{
//    public $binds;
//
//    public $instances;
//
//    public function bind($abstract, $concrete)
//    {
//        if ($concrete instanceof Closure) {
//            $this->binds[$abstract] = $concrete;
//        } else {
//            $this->instances[$abstract] = $concrete;
//        }
//    }
//
//    public function make($abstract, $parameters = [])
//    {
//        if (isset($this->instances[$abstract])) {
//            return $this->instances[$abstract];
//        }
//
//        array_unshift($parameters, $this);
//
//        return call_user_func_array($this->binds[$abstract], $parameters);
//    }
//}
//
//// 创建一个容器（后面称作超级工厂）
//$container = new Container;
//
//// 向该 超级工厂 添加 超人 的生产脚本
//$container->bind('superman', function($container, $moduleName) {
//    $container->name = 'Jack';
//    $moduleName->name = 'Jack';
//    return new Superman($container->make($moduleName));
//});
//
//// 向该 超级工厂 添加 超能力模组 的生产脚本
//$container->bind('xpower', function($container) {
//    $container->power = '100';
//    return new XPower;
//});
//
//// 同上
//$container->bind('ultrabomb', function($container) {
//    $container->power = '10000';
//    return new UltraBomb;
//});
//
//// ******************  华丽丽的分割线  **********************
//// 开始启动生产
//$superman_1 = $container->make('superman', 'xpower');
//$superman_2 = $container->make('superman', 'ultrabomb');
//$superman_3 = $container->make('superman', 'xpower');
//
////var_dump($container->binds['superman']);
```

set方式注册的，每次获取的时候都会重新实例化  

  

setShared方式的，则只实例化一次，也就是所谓的单例模式

  
  

  

