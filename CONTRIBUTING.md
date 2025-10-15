# 贡献指南

感谢您对 Tee ORM 的兴趣！我们欢迎任何形式的贡献。

## 开发环境设置

1. Fork 并 clone 项目：
```bash
git clone https://github.com/your-username/tee.git
cd tee
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 安装开发依赖：
```bash
pip install -r requirements-dev.txt
pip install -e .
```

## 代码规范

我们使用以下工具来保持代码质量：

- **Black**: 代码格式化
- **isort**: 导入语句排序
- **flake8**: 代码风格检查
- **mypy**: 类型检查

运行所有检查：
```bash
# 格式化代码
black tee tests
isort tee tests

# 检查代码风格
flake8 tee tests

# 类型检查
mypy tee
```

## 测试

运行测试：
```bash
pytest tests/ --cov=tee
```

确保所有测试通过，并且新功能有相应的测试覆盖。

## 提交流程

1. 创建功能分支：
```bash
git checkout -b feature/your-feature-name
```

2. 进行更改并提交：
```bash
git add .
git commit -m "feat: add your feature description"
```

3. 运行测试和代码检查：
```bash
pytest
black tee tests
flake8 tee tests
mypy tee
```

4. 推送分支并创建 Pull Request：
```bash
git push origin feature/your-feature-name
```

## 提交信息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 错误修复
- `docs:` 文档更新
- `style:` 代码风格调整
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

## 问题报告

请在提交 Issue 时包含：

1. 问题的详细描述
2. 复现步骤
3. 期望的行为
4. 实际的行为
5. 环境信息（Python版本、操作系统等）

## 功能请求

请在提交功能请求时包含：

1. 功能的详细描述
2. 使用场景
3. 可能的实现方案

## 代码审查

所有的代码更改都需要通过代码审查。请确保：

1. 代码符合项目的编码规范
2. 包含适当的测试
3. 更新相关文档
4. 通过所有 CI 检查

感谢您的贡献！