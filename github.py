from flask import Flask,render_template,request
import requests
app = Flask(__name__)
base_url = "https://api.github.com/users/"
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        # index.html dosyamızdaki form içerisinde bulunan name özelliğine göre bilgiyi aldık.
        githubname = request.form.get("githubname") 
        # github api ya get request atarak verileri almamız lazım.
        response_user = requests.get(base_url + githubname)
        response_repos = requests.get(base_url + githubname + "/repos")
        #response değerinden dönen verileri json olarak tutmamız gerekmektedir.
        user_info = response_user.json()
        repos = response_repos.json()
        if "message" in user_info:
            return render_template("index.html",error = "User not found.")
        else:
            return render_template("index.html",profile = user_info, repos=repos)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)