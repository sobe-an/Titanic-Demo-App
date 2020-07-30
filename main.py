# import requests
# import json
from bokeh.io import curdoc
from bokeh.layouts import column, layout, row
from bokeh.models import Div, TextInput, Paragraph, Button

pred1 = TextInput(value="1", title="Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd):",css_classes = ["form"])
pred2 = TextInput(value="F", title="Sex:",css_classes = ["form"])
pred3 = TextInput(value="24", title="Age (yrs):",css_classes = ["form"])
pred4 = TextInput(value="4", title="No. of Siblings/Spouse:",css_classes = ["form"])
pred5 = TextInput(value="4", title="No. of Parent/Children:",css_classes = ["form"])
pred6 = TextInput(value="300", title="Passenger Fare ($):",css_classes = ["form"])
pred7 = TextInput(value="C", title="Port of Embarkment (C = Cherbourg, Q = Queenstown, S = Southampton):",css_classes = ["form"])
button = Button(label="Predict!")

reply = 'Yes'
intro = "Will i survive the shipwreck?"
output = "Because the stars are in your favor, {} you will survive.".format(reply)

para1 = Paragraph(text=intro,width=200, height=30)
para2 = Paragraph(text=output,width=200, height=100)
replyview = row(para1, para2,css_classes = ["text-output"])

def get_passenger():
    passenger = {'Pclass':int(pred1.value),'Sex':str(pred2.value),'Age':int(pred3.value),'SibSp':int(pred4.value),'Parch':int(pred5.value),'Fare':float(pred6.value),'Embarked':str(pred7.value)}
    return passenger

def process_data():
    data = get_passenger()
    """
    url = 'http://0.0.0.0:5000/api/'

    j_data = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    print(r, r.text)
    """
    print(data)

button.on_click(process_data)


container = Div(text="""<style>
.bk-root::before {
    content:"Get Onboard!";
    font-size:24px;
}

.full-cont {
    margin:auto;
    width: 40%;
    height: 100%
}
.display-cont {
    margin:auto;
    height: 100%;
    top:10px;
    width: 40%;
    left: 35px;
    padding: 15px;
    background-color: #286aa6;
    box-shadow: black 1px 7px 9px 6px;
    } 

.bk.bk-btn-group {
    width:40%;
    height: 50px;
    margin:auto;
    margin-top:20px;
}

.bk-root .bk-btn-default {
    background-color:#b42454;
    font-size: 18px;
    color: black;
}
.form {
    margin: auto;
    width: 80%;
    height:20px;
}
.text-output {
    width: 100%;
    padding:15px;
    margin:auto;
    text-align:left;
    font-size: large;
}
</style>""")

content = column(pred1, pred2, pred3, pred4, pred5,pred6,pred7, button, replyview ,css_classes=['display-cont'])
L = layout(container,content, css_classes=['full-cont'])
L.sizing_mode = "scale_both"


curdoc().add_root(L)
curdoc().title = "Titanic"