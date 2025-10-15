"""
Tee ORM 基础使用示例
"""

from tee import Model, Int, Str, DateTime, set_default_db, transaction

# 配置数据库连接
set_default_db(
    host="localhost",
    port=3306,
    user="root", 
    password="password",
    database="example_db"
)

# 定义模型
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

def main():
    # 1. 插入数据
    print("=== 插入数据 ===")
    user_id = User.insert().execute({
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 25,
        "created_at": "2024-01-01 10:00:00"
    })
    print(f"插入用户，ID: {user_id}")
    
    # 2. 查询单个用户
    print("\n=== 查询单个用户 ===")
    user = User.select().eq(User.id, 1).one()
    if user:
        print(f"用户: {user.name}, 邮箱: {user.email}")
    
    # 3. 查询所有用户
    print("\n=== 查询所有用户 ===")
    users = User.select().list()
    for user in users:
        print(f"ID: {user.id}, 名字: {user.name}, 年龄: {user.age}")
    
    # 4. 条件查询
    print("\n=== 条件查询 ===")
    adult_users = User.select().gt(User.age, 18).list()
    print(f"成年用户数量: {len(adult_users)}")
    
    # 5. 更新数据
    print("\n=== 更新数据 ===")
    affected = User.update().eq(User.id, 1).set(age=26).execute()
    print(f"更新了 {affected} 条记录")
    
    # 6. 使用事务
    print("\n=== 事务示例 ===")
    try:
        with transaction():
            # 插入用户
            User.insert().execute({
                "name": "李四",
                "email": "lisi@example.com", 
                "age": 30,
                "created_at": "2024-01-02 10:00:00"
            })
            
            # 插入文章
            Post.insert().execute({
                "title": "我的第一篇文章",
                "content": "这是内容...",
                "user_id": 2,
                "created_at": "2024-01-02 11:00:00"
            })
            
        print("事务执行成功")
    except Exception as e:
        print(f"事务执行失败: {e}")
    
    # 7. 复杂查询
    print("\n=== 复杂查询 ===")
    users = (User.select()
             .ge(User.age, 18)
             .le(User.age, 65) 
             .like(User.name, "张")
             .desc(User.created_at)
             .limit(10)
             .list())
    
    for user in users:
        print(f"符合条件的用户: {user.name}")

if __name__ == "__main__":
    main()