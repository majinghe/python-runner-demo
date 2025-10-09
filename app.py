from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/github")
def hello():
    # 使用 render_template_string 直接写 HTML
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello GitHub Actions</title>
        <style>
            html, body {
                height: 100%;
                margin: 0;
            }
            body {
                display: flex;
                justify-content: center; /* 水平居中 */
                align-items: center;     /* 垂直居中 */
                font-size: 72px;         /* 字体大小 */
                font-family: Arial, sans-serif;
                background-color: #f0f0f0; /* 可选背景色 */
            }
        </style>
    </head>
    <body>
        Hello, GitHub Actions!!!!!!!!!!!!
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
