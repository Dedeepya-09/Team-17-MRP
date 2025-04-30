from flask import Flask, render_template, request, redirect, url_for
import recommender
import numpy as np

app = Flask(__name__)

def get_skill_averages(dataFrame):
    skills = ["HTML", "Python", "Java", "C", "JavaScript", "SQL"]
    skill_sums = {skill: 0 for skill in skills}
    count = 0
    cgpas = []
    for candidate in dataFrame.values():
        for skill in skills:
            skill_sums[skill] += candidate.get(skill, 0)
        cgpas.append(candidate.get("CGPA", 0))
        count += 1
    skill_avgs = {skill: round(skill_sums[skill] / count, 2) for skill in skills}
    return skill_avgs, cgpas

def get_proficiency_distribution(dataFrame):
    beginner, intermediate, advanced, expert = 0, 0, 0, 0
    
    for candidate in dataFrame.values():
        avg_skill = sum([candidate.get(skill, 0) for skill in ["HTML", "Python", "Java", "C", "JavaScript", "SQL"]]) / 6
        if avg_skill < 2:
            beginner += 1
        elif avg_skill < 3:
            intermediate += 1
        elif avg_skill < 4:
            advanced += 1
        else:
            expert += 1
            
    total = beginner + intermediate + advanced + expert
    return [
        round(beginner/total*100), 
        round(intermediate/total*100), 
        round(advanced/total*100), 
        round(expert/total*100)
    ]

@app.route('/')
def dashboard():
    try:
        skill_avgs, cgpas = get_skill_averages(recommender.dataFrame)
        bins = [0, 5, 6, 7, 8, 10]
        cgpa_hist = np.histogram(cgpas, bins=bins)[0].tolist()
        proficiency = get_proficiency_distribution(recommender.dataFrame)
        
        return render_template("index.html", 
                             active_page="dashboard",
                             skill_avgs=skill_avgs,
                             cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                             cgpa_hist=cgpa_hist,
                             proficiency=proficiency,
                             result=[])
    except Exception as e:
        return render_template("index.html", 
                             error=f"Dashboard error: {str(e)}",
                             active_page="dashboard")

@app.route('/filter', methods=['GET', 'POST'])
def filter_candidates():
    try:
        skill_avgs, cgpas = get_skill_averages(recommender.dataFrame)
        bins = [0, 5, 6, 7, 8, 10]
        cgpa_hist = np.histogram(cgpas, bins=bins)[0].tolist()
        proficiency = get_proficiency_distribution(recommender.dataFrame)
        
        if request.method == 'POST':
            try:
                form = request.form
                requirement = {
                    "REQUIREMENT": {
                        "HTML": int(form['html']),
                        "Python": int(form['python']),
                        "Java": int(form['java']),
                        "C": int(form['c']),
                        "JavaScript": int(form['javascript']),
                        "SQL": int(form['sql'])
                    }
                }
                num_candidates = int(form['candidate'])
                min_cgpa = float(form['cgpa'])
                
                raw_results = recommender.topMatches(requirement, recommender.dataFrame, 
                                                  "REQUIREMENT", num_candidates * 2)
                filtered_results = []
                for score, name in raw_results:
                    candidate = recommender.dataFrame[name]
                    if candidate.get("CGPA", 0.0) >= min_cgpa:
                        filtered_results.append((score, name, candidate["CGPA"]))
                    if len(filtered_results) >= num_candidates:
                        break
                
                return render_template("index.html", 
                                     active_page="filter",
                                     result=filtered_results,
                                     skill_avgs=skill_avgs,
                                     cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                                     cgpa_hist=cgpa_hist,
                                     proficiency=proficiency)
            except KeyError as e:
                return render_template("index.html", 
                                     error=f"Missing field: {str(e)}",
                                     active_page="filter",
                                     skill_avgs=skill_avgs,
                                     cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                                     cgpa_hist=cgpa_hist,
                                     proficiency=proficiency)
            except ValueError as e:
                return render_template("index.html", 
                                     error=f"Invalid input: {str(e)}",
                                     active_page="filter",
                                     skill_avgs=skill_avgs,
                                     cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                                     cgpa_hist=cgpa_hist,
                                     proficiency=proficiency)
        
        return render_template("index.html", 
                             active_page="filter",
                             skill_avgs=skill_avgs,
                             cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                             cgpa_hist=cgpa_hist,
                             proficiency=proficiency,
                             result=[])
    except Exception as e:
        return render_template("index.html", 
                             error=f"Filter error: {str(e)}",
                             active_page="filter")

@app.route('/skill-analysis')
def skill_analysis():
    try:
        skill_avgs, cgpas = get_skill_averages(recommender.dataFrame)
        bins = [0, 5, 6, 7, 8, 10]
        cgpa_hist = np.histogram(cgpas, bins=bins)[0].tolist()
        proficiency = get_proficiency_distribution(recommender.dataFrame)
        
        return render_template("index.html", 
                             active_page="skill_analysis",
                             skill_avgs=skill_avgs,
                             cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                             cgpa_hist=cgpa_hist,
                             proficiency=proficiency,
                             result=[])
    except Exception as e:
        return render_template("index.html", 
                             error=f"Skill analysis error: {str(e)}",
                             active_page="skill_analysis")

@app.route('/reports')
def reports():
    try:
        skill_avgs, cgpas = get_skill_averages(recommender.dataFrame)
        bins = [0, 5, 6, 7, 8, 10]
        cgpa_hist = np.histogram(cgpas, bins=bins)[0].tolist()
        proficiency = get_proficiency_distribution(recommender.dataFrame)
        
        return render_template("index.html", 
                             active_page="reports",
                             skill_avgs=skill_avgs,
                             cgpa_labels=["0-5", "5-6", "6-7", "7-8", "8-10"],
                             cgpa_hist=cgpa_hist,
                             proficiency=proficiency,
                             result=[])
    except Exception as e:
        return render_template("index.html", 
                             error=f"Reports error: {str(e)}",
                             active_page="reports")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', error="Page not found"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('index.html', error="Method not allowed - please use the form correctly"), 405

@app.errorhandler(500)
def server_error(e):
    return render_template('index.html', error=f"Server error: {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
