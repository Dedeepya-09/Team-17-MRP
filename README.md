# Team-17-MRP
This is the Team-17 Masters Research Project team Git Hub Account Repository
# Skill-Driven Job Navigator

A web-based platform that enables recruiters to filter, rank, and analyze candidates based on specific technical skill sets, streamlining the hiring process with an intuitive and data-driven approach.

## Project Description

The Skill-Driven Job Navigator is designed to address the challenges recruiters face when identifying the best candidates based on skill criteria. This platform enhances the hiring process by allowing recruiters to:

- Input and filter candidates by technical skills (e.g., Java, HTML, Python, SQL).
- Rank candidates based on specified skill preferences.
- Visualize candidate strengths and skill distribution through interactive charts.
- Improve decision-making with data-driven analytics.

### Key Features:

- **Skill-Based Candidate Filtering**: Allows recruiters to input specific skill criteria to filter candidates.
- **Candidate Ranking System**: Dynamically ranks applicants based on technical capabilities.
- **Interactive Data Visualization**: Provides charts and tables for a clear overview of candidate strengths and trends.
- **User-Friendly Navigation**: Intuitive sidebar navigation for easy access to core sections (Dashboard, Filter Candidates, Skill Analysis, and Reports).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Skill-Driven-Job-Navigator.git
cd Skill-Driven-Job-Navigator
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use 'venv\\Scripts\\activate'
```

3. Install dependencies:

```bash
pip install flask
```


## Usage

1. Start the application:

```bash
python main.py
```

2. Navigate to the dashboard in your web browser:

```
http://127.0.0.1:5000
```

3. Use the following main functionalities:

   - **Filter Candidates**: Input skill criteria (e.g., Java, HTML, Python) and click 'Submit' to rank candidates.
   - **Skill Analysis**: View candidate rankings and detailed skill metrics.
   - **Reports**: Analyze hiring trends and skill distributions via interactive charts.

## Features

- Intuitive skill-based filtering system.
- Dynamic candidate ranking by technical capabilities.
- Interactive visualization for better decision-making.
- User-friendly interface with clear navigation.

## Dashboard Preview


[![Watch the demo video](https://github.com/user-attachments/assets/a67ad30c-ba89-4040-a84c-dc2efc642b2d)](https://sluedu-my.sharepoint.com/:v:/g/personal/srisai_madamsatti_slu_edu/EQO7vRsEnNhHhBBE2jKqv-cBSdZCNAQLqHa5_QIT3htMyQ)



## Project Structure

Skill-Driven-Job-Navigator/
├── __pycache__/
│   └── recommender.cpython-313.pyc
├── templates/
│   └── index.html
├── venv/
├── 1000DATASET_CLEANED.json
├── main.py
├── package.json
├── package-locks.json
├── recommender.py


```
Skill-Driven-Job-Navigator/
├── data/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── requirements.txt
└── README.md
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to modify.

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

Special thanks to the project team members:

- Shiva Dutta Butta
- Dedeepya Cherukupalli
- Nikhithareddy Gaddam
- Vidya Sravanthi Garikapati
- Srisai Madamsetti

Project Advisor: Prof. Maria Weber (IS-5960-02 – Master’s Research Project)

