HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Demo</title>
    <style>
        body {
            margin: 0;
            background: #0066cc;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }

        .card {
            width: 900px;
            margin: auto;
            background: rgba(255,255,255,0.15);
            padding: 30px;
            border-radius: 15px;
        }

        .pipeline {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            margin-top: 40px;
            flex-wrap: wrap;
        }

        .pipeline img {
            width: 90px;
            height: 90px;
            background: white;
            border-radius: 10px;
            padding: 10px;
        }

        .arrow {
            font-size: 30px;
            font-weight: bold;
        }

        .footer {
            margin-top: 50px;
            font-size: 14px;
        }
    </style>
</head>
<body>

<div class="card">

    <h1>🚀 CI/CD Demo Project</h1>

    <h2>Version 2</h2>

    <p>
        Successfully deployed by <b>Debdip Ghosh</b>
    </p>

    <h3>CI/CD Pipeline Flow</h3>

    <div class="pipeline">

        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">

        <div class="arrow">→</div>

        <img src="https://www.jenkins.io/images/logos/jenkins/jenkins.svg">

        <div class="arrow">→</div>

        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg">

        <div class="arrow">→</div>

        <img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg">

        <div class="arrow">→</div>

        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg">

    </div>

    <h3 style="margin-top:40px;">
        Application Running Successfully ✅
    </h3>

</div>

<div class="footer">
    GitHub → Jenkins → Docker → Docker Hub → Kubernetes
</div>

</body>
</html>
"""
