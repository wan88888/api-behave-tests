# API Behave Tests

使用 Behave 框架测试 JSONPlaceholder API 的项目。

## 快速开始

```bash
# 安装依赖
make install

# 运行测试
make test
```

## 可用命令

```bash
make install      # 安装依赖
make test         # 运行测试
make test-verbose # 详细输出测试
make clean        # 清理生成文件
make lint         # 代码检查
make format       # 代码格式化
```

## 测试场景

- 获取所有帖子 (GET `/posts`)
- 获取特定用户 (GET `/users/1`)
- 创建新帖子 (POST `/posts`)

## CI/CD

项目配置了 GitHub Actions 工作流：
- 自动运行测试（支持 Python 3.8-3.11）
- 定时测试（工作日每天上午9点UTC）
- 测试结果报告

测试 API: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)