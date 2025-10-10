from app import app

def test_github_route():
    # 使用 Flask 提供的测试客户端
    client = app.test_client()
    response = client.get("/github")

    # 1. HTTP 状态码应该是 200
    assert response.status_code == 200

    # 2. 返回内容应包含 "Hello, GitHub Actions"
    assert b"Hello, GitHub Actions" in response.data
