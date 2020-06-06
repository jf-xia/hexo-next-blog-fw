---
title: "AI Code Level 1"
date: 2020-03-29 08:00:00
updated: 2020-04-10 10:09:33
tags: ["AI","Notes","Study"]
---

[AI-Edu](https://github.com/Microsoft/ai-edu)

## 房价预测问题

如果用传统的数学方法解决这个问题，我们可以使用正规方程，从而可以得到数学解析解，然后再使用神经网络方式来求得近似解，从而比较两者的精度，再进一步调试神经网络的参数，达到学习的目的。

我们不妨先把两种方式在这里做一个对比，读者阅读并运行代码，得到结果后，再回到这里来仔细体会表5-3中的比较项。

表5-3 两种方法的比较

|方法|正规方程|梯度下降|
|---|-----|-----|
|原理|几次矩阵运算|多次迭代|
|特殊要求|$X^TX$的逆矩阵存在|需要确定学习率|
|复杂度|$O(n^3)$|$O(n^2)$|
|适用样本数|$m \lt 10000$|$m \ge 10000$|


DialogFlow，Python 和 Flask 打造 ChatBot
https://github.com/virgili0/Virgilio/blob/master/zh-CN/Topics/DialogFlow.md

Object Instance Segmentation using TensorFlow Framework and Cloud GPU Technology
https://github.com/virgili0/Virgilio/blob/master/zh-CN/Topics/Computer%20Vision/Object_Instance_Segmentation_using_TensorFlow_Framework_and_Cloud_GPU_Technology.ipynb