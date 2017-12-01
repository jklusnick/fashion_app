from flask import Flask, render_template, request, url_for
app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def hello():
	global tasks
	if request.method == "POST":
		# print request.args
		# addButton = request.args.get('addButton', '')
		# deleteButton = request.args.get('deleteButton', '')
		if "poop1" in request.form:
			tasks.append(request.form["todo"])
		elif "poop2" in request.form:
			n = int(request.form["delete"]) - 1
			if n is not None and 0 <= n <= len(tasks) - 1 and len(tasks) > 0:
				tasks.remove(tasks[n])
			elif request.form["delete"] < 1:
				print "cant do that"

	return render_template("first.html", tasks=tasks, url_for=url_for)