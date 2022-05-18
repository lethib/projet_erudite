from flask import *
import pandas as pd
from function import *

app = Flask(__name__)
app.secret_key = "soso_erudite"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projet", methods=["POST","GET"])
def projet():
    if request.method == "POST":
        project_info = request.form
        print(project_info)
        if project_info["rep-correcte"] == 'on':
            dic = {}
            for info in project_info:
                dic[info] = [project_info[info]]
            df = pd.DataFrame(dic)
            head = [info_name for info_name in dic.keys()]
            print(df)
            row_to_write = empty_row('info_projet.xlsx')
            with pd.ExcelWriter('info_projet.xlsx', mode='a',engine='openpyxl', if_sheet_exists = 'overlay') as writer:
                df.to_excel(writer, 'Infos', header=head, startrow=row_to_write)
            return render_template("saved_answers.html")
        else:
            return render_template("projet.html")
    else:
        return render_template("projet.html")

@app.route("/plans")
def plans():
    return render_template("plans.html")

@app.route("/profil-client")
def profil_client():
    return render_template("profil_client.html")

@app.route("/carnet-bord")
def carnet_bord():
    return render_template("carnet_bord.html")

if __name__ == '__main__':
    app.run(debug=True)