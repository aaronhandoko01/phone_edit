from flask import Flask,render_template,request, flash, redirect, url_for
import pandas as pd
 
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
 
def change_num(num):
    print(num)
    num = "".join(num.split())
    num = num.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
    final = num[:2] + "-" + num[2:]
    return final

@app.route('/')
def form():
    return render_template('homepage.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        try:
            phone_raw = request.form.get("phone")
            ls_raw = phone_raw.split("\n")
            df = pd.DataFrame(ls_raw,columns = ["Phone Number"] )
            x = df["Phone Number"].apply(change_num)
            x.to_clipboard(excel = True, index = False, header = False)

            flash('The new phone number has been copied to clipboard')
            return redirect(url_for('form'))
        except Exception as e:
            print(e)
        return
    if request.method == 'GET':
        form_data = request.form
        app.logger.info(form_data)
        return "GET CHECK CONSOLE"
        # return render_template('data.html',form_data = form_data)
 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
 
# app.run(host='localhost', port=5000)