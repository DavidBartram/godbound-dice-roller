
# Godbound damage roller Flask App

from flask import Flask, request
from processing import rolldice, validate_roll


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])

def roller_page():

   if request.method == "POST":

        multiple = None
        result = ''
        num_targets = request.form["num_targets"]

        if num_targets.isdigit():
            num_targets = int(num_targets)
        else:
            num_targets = 1 #default to one target if the user puts something silly but not empty string into the number of targets field


        if num_targets==1:
            multiple = False
        elif num_targets>20:
            num_targets = 20
        else:
            multiple = True

        roll = request.form["roll"]

        valid = validate_roll(roll)

        if (roll=='' or num_targets==0 or not valid):
            result = "You have not entered a valid roll. Please click New Roll and input a roll such as 4d10+3 or d8 - 2."
            return '''
                <html>
                    <body>
                        <h style="font: bold 30px arial">Godbound Damage Roller</h>
                        <p style= "font: 25px arial">{result}</p>

                        <form action="/">
                            <p><input type="submit" style="margin-left: 2em; font: 25px arial" value="New Roll" /></p>
                        </form>
                    </body>
                </html>
            '''.format(result = result)

        else:
            for i in range(1,(num_targets+1)):
                result = result + rolldice(roll, multiple, i)

            return '''
                <html>
                    <body>
                        <h style="font: bold 30px arial">Godbound Damage Roller</h>
                        <p style= "font: 25px arial">{result}</p>
                        <form action="/">
                            <p><input type="submit" style="margin-left: 2em; font: 25px arial" value="New Roll" /></p>
                        </form>
                        <button onClick="window.location.reload();" style="margin-left:2em ;font: 25px arial">Reroll</button>
                    </body>
                </html>
            '''.format(result = result)


   else:

    return '''
            <html>
            <body>
                <h style="font: bold 30px arial">Godbound Damage Roller</h>
                <form method="post" action=".">
                    <p style ="font: 25px arial">Damage roll: <input style="font: 25px arial" name="roll" /></p>
                    <p style ="font:25px arial"># Targets: <input style="font: 25px arial" name="num_targets" value="1" /></p>
                    <p><input type="submit" style="font: 25px arial" value="Roll damage" /></p>
                </form>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)