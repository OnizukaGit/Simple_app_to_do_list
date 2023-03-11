from flask import Flask, render_template, request, redirect, url_for
import sql_engine

app = Flask(__name__)


@app.route("/")
def task_details():
    db = "to_do_list_db"
    sql_code = "select id, name, task from to_do_list"
    result = sql_engine.execute_sql(db, sql_code)
    return render_template("index.html", result=result)


@app.route("/add", methods=['GET', 'POST'])
def add_task():
    if request.method == "GET":
        return render_template('add.html')
    else:
        name = request.form.get('name')
        task = request.form.get('task')
        db = "to_do_list_db"
        sql_code = "INSERT INTO to_do_list (name,task) VALUES (%s,%s)"
        params = (name, task)
        sql_engine.execute_sql(db, sql_code, params)
        return redirect(url_for('task_details'))


@app.route("/update/<int:task_id>/", methods=['GET', 'POST'])
def update_task(task_id):
    if request.method == "GET":
        db = "to_do_list_db"
        sql_code = "SELECT * FROM to_do_list WHERE id=%s"
        params = (task_id,)
        result = sql_engine.execute_sql(db, sql_code, params)
        name = result[0][1]
        task = result[0][2]
        return render_template('update.html', name=name, task=task, id=task_id)
    if request.method == "POST":
        db = "to_do_list_db"
        name = request.form.get('name')
        task = request.form.get('task')
        sql_code = "UPDATE to_do_list SET name=%s, task=%s WHERE id=%s"
        params = (name, task, task_id)
        sql_engine.execute_sql(db, sql_code, params)
        return redirect(url_for('task_details'))


@app.route("/delete/<int:task_id>", methods=['POST', 'DELETE'])
def delete_task(task_id):
    if request.method == "POST":
        method = request.form.get('_method', '').upper()
        if method == "DELETE":
            db = "to_do_list_db"
            sql_code = "DELETE FROM to_do_list WHERE id=%s"
            params = (task_id,)
            sql_engine.execute_sql(db, sql_code, params)
        return redirect(url_for('task_details'))


if __name__ == '__main__':
    app.run(debug=True)
