## HTTP API  Lambda autherizer 配置

1. 创建 Lambda 函数，内容参考 [lambda.py](./lambda.py)

2. 创建 IAM Role，允许 API Gateway 调用 authorizer Lambda

3. API Gateway 配置

![](imgs/2023-10-12-16-17-29.png)

![](imgs/2023-10-12-16-18-02.png)

![](imgs/2023-10-12-16-19-22.png)

![](imgs/2023-10-12-16-22-55.png)

4. 验证校验效果

请求中未包含校验指定的信息
![](2023-10-12-16-26-33.png)

校验未通过
![](2023-10-12-16-26-09.png)

校验通过
![](2023-10-12-16-27-08.png)
