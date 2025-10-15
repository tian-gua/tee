.PHONY: install install-dev test lint format type-check clean build upload help

help:  ## 显示帮助信息
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## 安装包
	pip install -e .

install-dev:  ## 安装开发依赖
	pip install -r requirements-dev.txt
	pip install -e .

test:  ## 运行测试
	pytest tests/ --cov=tee --cov-report=term-missing --cov-report=html

lint:  ## 代码风格检查
	flake8 tee tests

format:  ## 格式化代码
	black tee tests
	isort tee tests

type-check:  ## 类型检查
	mypy tee

clean:  ## 清理构建文件
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build:  ## 构建包
	python -m build

upload:  ## 上传到 PyPI
	twine upload dist/*

check-all: lint type-check test  ## 运行所有检查

dev-setup: install-dev  ## 设置开发环境
	@echo "开发环境设置完成！"
	@echo "运行 'make help' 查看可用命令"