import flask
import subprocess
from flask import Flask, render_template, request
import re

app = Flask(__name__)

numbat = "mentalsuffering.nbt"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pmass = request.form.get("pmass")  
        pheight = request.form.get("pheight")  

        with open(numbat, 'r') as infile:
            file_content = infile.read()

        file_content = re.sub(r"(let\s+tmass\s*=\s*)\d+(\.\d+)?", r"\g<1>" + str(pmass), file_content)
        file_content = re.sub(r"(let\s+theight\s*=\s*)\d+(\.\d+)?", r"\g<1>" + str(pheight), file_content)

        with open(numbat, 'w') as ofile:
            ofile.write(file_content)

        result = subprocess.run(["numbat", numbat], capture_output=True, text=True, shell=True)

        return render_template("index.html", result=result.stdout, pmass=pmass, pheight=pheight)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
