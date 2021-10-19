# using flask
import base64
from io import BytesIO
import pandas as pd
from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

app = Flask(__name__)

df=pd.read_csv("data.csv") #load the dataset
#df is the data frame here(data set)
df['total']=df.iloc[:,-12:].sum(axis=1)  #new col for total crimes
d=df[:-38] #to drop total crime rows
#d is the updated data set 

list_state_ut = d['STATE/UT'].tolist()
list_state_ut = list_state_ut[0:36:]     #total state/ut coloumn
list_state_ut.remove('TOTAL (STATES)')   #particular state and UT only
list_ut = list_state_ut[28:36:]     #particular ut
list_state = list_state_ut[:28:]    #particular state
crime_head = d['CRIME HEAD'].unique()    #array of all crime heads
crime_head = crime_head.tolist()        #same as above in list particular crime   

font1 = {'family':'serif','color':'orange','size':20}
font2 = {'family':'serif','color':'red','size':15}
sl_no_crime=[]
for i in range(1, 13):
    sl_no_crime.append(i)

sl_no_state=[]
for i in range(1, 36):
    sl_no_state.append(i)

@app.route("/")
def home():
    return render_template('home.html')

#####################################################################################################

# first drop down list menu

@app.route("/crime_infanticide")
def crime_infanticide():
    temp1 = d[d['CRIME HEAD'].str.contains('INFANTICIDE')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]])
    temp2['sl_no']=sl_no_state    
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    #plt.tight_layout()
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("INFANTICIDE", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_murder_of_children")
def crime_murder_of_children():
    temp1 = d[d['CRIME HEAD'].str.contains('MURDER OF CHILDREN')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("MURDER OF CHILDREN", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_rape_of_children")
def crime_rape_of_children():
    temp1 = d[d['CRIME HEAD'].str.contains('RAPE OF CHILDREN')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state    
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("RAPE OF CHILDREN", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)
    

@app.route("/crime_kidnapping_and_abduction_of_children")
def crime_kidnapping_and_abduction_of_children():
    temp1 = d[d['CRIME HEAD'].str.contains('KIDNAPPING and ABDUCTION OF CHILDREN')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("KIDNAPPING and ABDUCTION OF CHILDREN", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_foeticide")
def crime_foeticide():
    temp1 = d[d['CRIME HEAD'].str.contains('FOETICIDE')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("FOETICIDE", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_abetment_of_suicide")
def crime_abetment_of_suicide():
    temp1 = d[d['CRIME HEAD'].str.contains('ABETMENT OF SUICIDE')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state  
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("ABETMENT OF SUICIDE", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_exposure_and_abandonment")
def crime_exposure_and_abandonment():
    temp1 = d[d['CRIME HEAD'].str.contains('EXPOSURE AND ABANDONMENT')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("EXPOSURE AND ABANDONMENT", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_procuration_of_minor_girls")
def crime_procuration_of_minor_girls():
    temp1 = d[d['CRIME HEAD'].str.contains('PROCURATION OF MINOR GILRS')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("PROCURATION OF MINOR GILRS", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_buying_of_girls_for_prostitution")
def crime_buying_of_girls_for_prostitution():
    temp1 = d[d['CRIME HEAD'].str.contains('BUYING OF GIRLS FOR PROSTITUTION')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state  
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("BUYING OF GIRLS FOR PROSTITUTION", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_selling_of_girls_for_prostitution")
def crime_selling_of_girls_for_prostitution():
    temp1 = d[d['CRIME HEAD'].str.contains('SELLING OF GIRLS FOR PROSTITUTION')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state 
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("SELLING OF GIRLS FOR PROSTITUTION", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_prohibition_of_child_marriage_act")
def crime_prohibition_of_child_marriage_act():
    temp1 = d[d['CRIME HEAD'].str.contains('PROHIBITION OF CHILD MARRIAGE ACT')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state  
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("PROHIBITION OF CHILD MARRIAGE ACT", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/crime_other_crimes_against_children")
def crime_other_crimes_against_children():
    temp1 = d[d['CRIME HEAD'].str.contains('OTHER CRIMES AGAINST CHILDREN')] 
    temp2 = temp1.drop(temp1.index[[-1,-2,-10]]) 
    temp2['sl_no']=sl_no_state   
    temp2.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,8))
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.xticks(rotation='horizontal')
    plt.title("OTHER CRIMES AGAINST CHILDREN", fontdict = font1)
    plt.xlabel("LIST OF STATES/UT", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)

@app.route("/Total_Crime")     
def total_crime():
    temp1 = d[d['STATE/UT'] == 'TOTAL (ALL-INDIA)']
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TOTAL CRIMES", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/INDIA_CRIME_CHART")         #error in this code as of 17th oct 2021
def INDIA_CRIME_CHART():
    totalINDIA = d[d['STATE/UT'] == 'TOTAL (ALL-INDIA)']
    plt.xticks(rotation='vertical')  #for labeling the values vertically
    plt.bar(x="CRIME HEAD", height="total", width=0.8,color='red', bottom=None, align='center', data=totalINDIA)
    plt.grid(b=True, color='r',alpha=0.5)

    plt.title("INDIA CRIME CHART", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    #plt.show()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state_ut)
    
####################################################################################################

# second drop down list menu

@app.route("/ANDHRA_PRADESH")
def ANDHRA_PRADESH():
    temp1 = d[d['STATE/UT'].str.contains('ANDHRA PRADESH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("ANDHRA PRADESH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/ARUNACHAL_PRADESH")
def ARUNACHAL_PRADESH():
    temp1 = d[d['STATE/UT'].str.contains('ARUNACHAL PRADESH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("ARUNACHAL PRADESH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/ASSAM")
def ASSAM():
    temp1 = d[d['STATE/UT'].str.contains('ASSAM')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("ASSAM", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/BIHAR")
def BIHAR():
    temp1 = d[d['STATE/UT'].str.contains('BIHAR')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("BIHAR", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/CHHATTISGARH")
def CHHATTISGARH():
    temp1 = d[d['STATE/UT'].str.contains('CHHATTISGARH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("CHHATTISGARH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/GOA")
def GOA():
    temp1 = d[d['STATE/UT'].str.contains('GOA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("GOA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/GUJARAT")
def GUJARAT():
    temp1 = d[d['STATE/UT'].str.contains('GUJARAT')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("GUJARAT", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/HARYANA")
def HARYANA():
    temp1 = d[d['STATE/UT'].str.contains('HARYANA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("HARYANA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/HIMACHAL_PRADESH")
def HIMACHAL_PRADESH():
    temp1 = d[d['STATE/UT'].str.contains('HIMACHAL PRADESH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("HIMACHAL PRADESH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/JAMMU_and_KASHMIR")
def JAMMU_and_KASHMIR():
    temp1 = d[d['STATE/UT'].str.contains('JAMMU & KASHMIR')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("JAMMU & KASHMIR", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/JHARKHAND")
def JHARKHAND():
    temp1 = d[d['STATE/UT'].str.contains('JHARKHAND')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("JHARKHAND", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/KARNATAKA")
def KARNATAKA():
    temp1 = d[d['STATE/UT'].str.contains('KARNATAKA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("KARNATAKA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/KERALA")
def KERALA():
    temp1 = d[d['STATE/UT'].str.contains('KERALA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("KERALA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/MADHYA_PRADESH")
def MADHYA_PRADESH():
    temp1 = d[d['STATE/UT'].str.contains('MADHYA PRADESH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("MADHYA PRADESH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/MAHARASHTRA")
def MAHARASHTRA(): 
    temp1 = d[d['STATE/UT'].str.contains('MAHARASHTRA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("MAHARASHTRA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/MANIPUR")
def MANIPUR():
    temp1 = d[d['STATE/UT'].str.contains('MANIPUR')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("MANIPUR", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/MEGHALAYA")
def MEGHALAYA():
    temp1 = d[d['STATE/UT'].str.contains('MEGHALAYA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("MEGHALAYA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/MIZORAM")
def MIZORAM():
    temp1 = d[d['STATE/UT'].str.contains('MIZORAM')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("MIZORAM", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/NAGALAND")
def NAGALAND():
    temp1 = d[d['STATE/UT'].str.contains('NAGALAND')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("NAGALAND", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/ODISHA")
def ODISHA():
    temp1 = d[d['STATE/UT'].str.contains('ODISHA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("ODISHA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/PUNJAB")
def PUNJAB():
    temp1 = d[d['STATE/UT'].str.contains('PUNJAB')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("PUNJAB", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/RAJASTHAN")
def RAJASTHAN():
    temp1 = d[d['STATE/UT'].str.contains('RAJASTHAN')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("RAJASTHAN", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/SIKKIM")
def SIKKIM():
    temp1 = d[d['STATE/UT'].str.contains('SIKKIM')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("SIKKIM", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/TAMIL_NADU")
def TAMIL_NADU():
    temp1 = d[d['STATE/UT'].str.contains('TAMIL NADU')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TAMIL NADU", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/TRIPURA")
def TRIPURA():
    temp1 = d[d['STATE/UT'].str.contains('TRIPURA')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TRIPURA", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/UTTAR_PRADESH")
def UTTAR_PRADESH():
    temp1 = d[d['STATE/UT'].str.contains('UTTAR PRADESH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("UTTAR PRADESH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/UTTARAKHAND")
def UTTARAKHAND():
    temp1 = d[d['STATE/UT'].str.contains('UTTARAKHAND')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("UTTARAKHAND", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/WEST_BENGAL")
def WEST_BENGAL():
    temp1 = d[d['STATE/UT'].str.contains('WEST BENGAL')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("WEST BENGAL", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)
    
@app.route("/A_and_N_ISLANDS")
def A_and_N_ISLANDS():
    temp1 = d[d['STATE/UT'].str.contains('A & N ISLANDS')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("A & N ISLANDS", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/CHANDIGARH")
def CHANDIGARH():
    temp1 = d[d['STATE/UT'].str.contains('CHANDIGARH')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("CHANDIGARH", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/D_and_N_HAVELI")
def D_and_N_HAVELI():
    temp1 = d[d['STATE/UT'].str.contains('D & N HAVELI')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("D & N HAVELI", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/DAMAN_and_DIU")
def DAMAN_and_DIU():
    temp1 = d[d['STATE/UT'].str.contains('DAMAN & DIU')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("DAMAN & DIU", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/DELHI")
def DELHI():
    temp1 = d[d['STATE/UT'].str.contains('DELHI')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("DELHI", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/LAKSHADWEEP")
def LAKSHADWEEP():
    temp1 = d[d['STATE/UT'].str.contains('LAKSHADWEEP')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("LAKSHADWEEP", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/PUDUCHERRY")
def PUDUCHERRY():
    temp1 = d[d['STATE/UT'].str.contains('PUDUCHERRY')] 
    temp1['sl_no']=sl_no_crime
    temp1.plot(kind='bar',x='sl_no',y='total',color='red',figsize=(8,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("PUDUCHERRY", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/All_States")       
def All_States():
    temp1 = d[d['STATE/UT'].str.contains('ANDHRA PRADESH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl=[ap]
    temp1 = d[d['STATE/UT'].str.contains('ARUNACHAL PRADESH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('ASSAM')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('BIHAR')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('CHHATTISGARH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('GOA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('GUJARAT')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('HARYANA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('HIMACHAL PRADESH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('JAMMU & KASHMIR')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('JHARKHAND')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('KARNATAKA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('KERALA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('MADHYA PRADESH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('MAHARASHTRA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('MANIPUR')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('MEGHALAYA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('MIZORAM')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)  
    temp1 = d[d['STATE/UT'].str.contains('NAGALAND')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('ODISHA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('PUNJAB')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('RAJASTHAN')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('SIKKIM')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('TAMIL NADU')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('TRIPURA')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('UTTAR PRADESH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('UTTARAKHAND')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('WEST BENGAL')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    data = {'TOTAL':tl, 'sl_no':sl_no_state[:28:]}
    ts=pd.DataFrame(data)
    ts.plot(kind='bar',x='sl_no',y='TOTAL',color='red',figsize=(8,8))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TOTAL STATES", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_state)
    
@app.route("/All_UT")         
def All_UT():
    temp1 = d[d['STATE/UT'].str.contains('A & N ISLANDS')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl=[ap]
    temp1 = d[d['STATE/UT'].str.contains('CHANDIGARH')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('D & N HAVELI')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('DAMAN & DIU')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('DELHI')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('LAKSHADWEEP')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    temp1 = d[d['STATE/UT'].str.contains('PUDUCHERRY')] 
    ap=temp1.sum(axis=0)
    ap=ap['total']
    tl.append(ap)
    sl_no_ut=[]
    for i in range(1, 8):
        sl_no_ut.append(i)
    data = {'TOTAL':tl, 'sl_no':sl_no_ut}
    tu=pd.DataFrame(data)
    tu.plot(kind='bar',x='sl_no',y='TOTAL',color='red',figsize=(5,5))
    plt.xticks(rotation='horizontal')
    plt.grid(b=True, color='purple',alpha=0.5)
    plt.title("TOTAL UNION TERRITORY", fontdict = font1)
    plt.xlabel("LIST OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIMES", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=list_ut)

#####################################################################################################

#third dropdown menu list

@app.route("/crime_2001")
def crime_2001():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2001']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2001',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2001", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2002")
def crime_2002():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2002']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2002',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2002", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2003")
def crime_2003():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2003']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2003',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2003", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2004")
def crime_2004():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2004']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2004',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2004", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2005")
def crime_2005():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2005']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2005',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2005", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2006")
def crime_2006():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2006']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2006',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2006", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2007")
def crime_2007():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2007']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2007',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2007", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2008")
def crime_2008():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2008']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2008',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2008", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2009")
def crime_2009():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2009']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2009',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2009", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2010")
def crime_2010():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2010']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2010',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2010", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2011")
def crime_2011():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2011']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2011',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2011", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

@app.route("/crime_2012")
def crime_2012():
    y=d[d['STATE/UT'].str.contains('ALL-INDIA')]
    sc=y.loc[:,['CRIME HEAD','2012']]
    sc['sln']=sl_no_crime
    sc.plot(kind='bar',x='sln',y='2012',color='red')
    plt.xticks(rotation="horizontal")
    plt.grid(b=True, color='grey',alpha=0.5)
    plt.title("Year 2012", fontdict = font1)
    plt.xlabel("TYPE OF CRIMES", fontdict = font2)
    plt.ylabel("RATE OF CRIME", fontdict = font2)
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('showData.html', data=data, html_var=crime_head)

####################################################################################################

if __name__ == "__main__": 
    app.run(debug=True) 