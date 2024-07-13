from flask import Flask, render_template, url_for, request
from utils.giftAdviser import suggest_folder
import glob
import argparse

app=Flask(__name__)

ap = argparse.ArgumentParser()
ap.add_argument("-host", "--host", type=str, required=False,
                help="Enter host domain name - default localhost", default=None)
ap.add_argument("-p", "--port", type=int, required=False,
                help="Enter port number - default localhost", default=3000)
args = vars(ap.parse_args())



@app.route('/', methods = ['GET', 'POST'])
def index():
	a = url_for('static', filename= 'img/vislogo.png')
	aa = url_for('static', filename= 'img/img_lights.jpg')
	ca = url_for('static', filename= 'img/img_snow.jpg')
	# return a
	recomm_files=[]
	al=[]
	cat_l=[]
	data_dict = {}

	if args['host']==None:
		host='localhost'
	else:
		host=args['host']

	port = args['port']


	url = f"http://{host}:{port}/"

	for i in range(19):
		recomm_files.append(a)
		al.append(aa)
		cat_l.append(ca)

	prefix='static/assets'
	all_file=[]
	for filename in glob.iglob(prefix+'/**/*.jpg',recursive = True):
		all_file.append(filename)
		# print(filename)


	if request.method == 'POST':
		Gender= request.form['Gender']
		Age= request.form['Age']
		Profession=request.form['Profession']
		print(Gender)
		
	
		data_dict['Gender'] = Gender
		data_dict['Profession'] = Profession
		data_dict['Age'] = Age
		recomm_files=suggest_folder(data_dict)



	return render_template('index.html',  img_list=recomm_files, all_list=all_file, result=data_dict, cat_list=cat_l,url=url)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=args['port'],debug=True)