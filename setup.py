from setuptools import setup

setup(
    name="lung_cancer_prediction",
    version="1.0.0",
    packages=["CODE.FRONT_END"],
    package_dir={"CODE.FRONT_END": "CODE/FRONT_END"},
    include_package_data=True,
    install_requires=[
        'Flask==2.0.1',
        'Flask-SQLAlchemy==2.5.1',
        'Flask-Login==0.5.0',
        'Flask-Cors==3.0.10',
        'Werkzeug==2.0.3',
        'Jinja2==3.0.3',
        'itsdangerous==2.0.1',
        'click==8.0.4',
        'pandas==1.3.3',
        'numpy==1.21.6',
        'scipy==1.7.3',
        'scikit-learn==0.24.2',
        'joblib==1.1.0',
        'python-dotenv==0.19.2',
        'aws-wsgi==0.2.3',
    ],
    python_requires='>=3.7',
    setup_requires=[
        'setuptools>=65.5.0',
        'wheel>=0.38.4'
    ],
)
