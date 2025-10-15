# Tee

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

一个小巧的 Python ORM 框架，可以理解成带有类型系统的 Peewee。Tee 专注于提供简洁、类型安全的数据库操作体验。

## ✨ 特性

- 🎯 **类型安全**: 完整的类型提示支持，IDE 友好
- 🚀 **简洁语法**: 链式调用，直观易懂的 API 设计
- 🔧 **轻量级**: 最小化依赖，核心功能专注
- 🎪 **灵活查询**: 支持复杂条件查询和排序
- 🔄 **事务支持**: 内置事务管理
- 📊 **多数据库**: 支持多数据库连接配置

## 📦 安装

```bash
pip install tee-orm-tiangua
```

## 🚀 快速开始

### 1. 配置数据库连接

```python
from tee import set_default_db

# 配置默认数据库
set_default_db(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="test_db"
)
```

### 2. 定义模型

```python
from tee import Model, Int, Str, DateTime

class User(Model):
    id = Int()
    name = Str()
    email = Str()
    age = Int()
    created_at = DateTime()

class Post(Model):
    id = Int()
    title = Str()
    content = Str()
    user_id = Int()
    created_at = DateTime()
```

### 3. 查询操作

```python
# 查询单条记录
user = User.select().eq(User.id, 1).get()
print(user.name)

# 查询多条记录
users = User.select().gt(User.age, 18).list()

# 条件查询
adult_users = (User.select()
               .gt(User.age, 18)
               .like(User.name, "张")
               .list())

# 排序和分页
users = (User.select()
         .desc(User.created_at)
         .limit(10)
         .offset(0)
         .list())

# 查询指定字段
users = User.select(["id", "name", "email"]).list()

# 安全的单条查询（不存在时返回 None）
user = User.select().eq(User.email, "test@example.com").one()
if user:
    print(f"Found user: {user.name}")
```

### 4. 新增操作

```python
# 单条插入
affected_rows = User.insert().execute({
    "name": "张三",
    "email": "zhangsan@example.com", 
    "age": 25,
    "created_at": "2024-01-01 00:00:00"
})

# 使用模型对象插入
user = User(name="李四", email="lisi@example.com", age=30)
User.insert().execute(user)

# 批量插入
users_data = [
    {"name": "王五", "email": "wangwu@example.com", "age": 28},
    {"name": "赵六", "email": "zhaoliu@example.com", "age": 32}
]
User.insert().execute_bulk(users_data)

# 插入时处理重复键
User.insert().execute(
    {"name": "张三", "email": "zhangsan@example.com"}, 
    duplicate_key_update=["name"]  # 重复时更新 name 字段
)
```

### 5. 更新操作

```python
# 条件更新
affected_rows = (User.update()
                 .eq(User.id, 1)
                 .set(name="新名字", age=26)
                 .execute())

# 批量更新
(User.update()
 .gt(User.age, 18)
 .set({"status": "adult"})
 .execute())
```

### 6. 删除操作

```python
# 条件删除
affected_rows = (User.delete()
                 .eq(User.id, 1)
                 .execute())

# 批量删除
(User.delete()
 .lt(User.age, 18)
 .execute())
```

## 🔧 高级用法

### 事务管理

```python
from tee import transaction

# 自动事务管理
with transaction():
    User.insert().execute({"name": "事务用户", "email": "tx@example.com"})
    Post.insert().execute({"title": "事务文章", "user_id": 1})
    # 如果发生异常，自动回滚
```

### 多数据库支持

```python
from tee import set_db

# 配置多个数据库
set_db("analytics", 
       host="analytics-host", 
       port=3306,
       user="analytics_user", 
       password="password",
       database="analytics_db")

# 在特定数据库上执行操作
users = User.select().list()  # 使用默认数据库
```

### 复杂查询条件

```python
from tee.where import Or

# OR 条件查询
or_condition = Or().eq(User.age, 25).eq(User.age, 30)
users = User.select().or_(or_condition).list()

# 多种操作符
users = (User.select()
         .ge(User.age, 18)        # 大于等于
         .le(User.age, 65)        # 小于等于
         .ne(User.status, "banned") # 不等于
         .in_(User.role, ["admin", "user"])  # IN 操作
         .like(User.name, "张")    # LIKE 搜索
         .list())
```

### 模型方法

```python
# 转换为字典
user_dict = user.to_dict()

# 转换为 JSON
user_json = user.to_json()

# 获取表名（自动转换为 snake_case）
table_name = User.get_table_name()  # "user"

# 获取字段名列表
field_names = User.get_field_names()  # ["id", "name", "email", "age", "created_at"]
```

## 🎯 类型系统

Tee 提供完整的类型提示支持，让你的 IDE 能够提供准确的代码补全和类型检查：

```python
from typing import Optional

# 查询返回带类型的对象
user: Optional[User] = User.select().eq(User.id, 1).one()
if user:
    # IDE 能够识别 user.name 的类型为 Optional[str]
    print(user.name.upper())  # 类型安全

# 列表查询返回类型化列表
users: List[User] = User.select().list()
```

## 📝 支持的字段类型

- `Int()` - 整数字段
- `Str()` - 字符串字段  
- `Float()` - 浮点数字段
- `DateTime()` - 日期时间字段

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🔗 相关链接

- [PyMySQL](https://github.com/PyMySQL/PyMySQL) - MySQL 数据库连接器
- [Peewee](https://github.com/coleifer/peewee) - 灵感来源

---

Made with ❤️ by [tian-gua](https://github.com/tian-gua)