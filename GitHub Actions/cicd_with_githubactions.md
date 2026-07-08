You Can absolutely use the SAME GitHub repo for both Jenkins and GitHub Actions.  
But it can do a build conflict , so you need to disable webhook (Jenkins) 

Better To create a diff repo  

### Clone the Repo we have used for jenkins  and modify and upadte to a diffrent repo
```
git clone https://github.com/<githubuser>/< your jenkins cicd repo >

rm -rf .git/refs/remotes/origin 

git remote remove origin 

git remote add origin https://github.com/<githubuser>/< cicd gitaction repo>

git push -u origin main 

git pull origin main --allow-unrelated-histories 

git remote –v 

git remote show origin 

git push -u origin main 
```

Now you can see the new repo with all the contents  

## GitHub Actions CI/CD setup 


### Create Workflow File

Your repo should have: <cicd gitaction repo>/.github/workflows/cicd.yaml 
 .github/workflows/cicd.yaml 

### Add GitHub Secrets 

Go to:    GitHub → Repo → Settings →security -> Secrets & variables → Actions ->  New repository secret  

Add:  DockerHub Credentials 

DOCKER_USERNAME:  your username 
DOCKER_PASSWORD: your token not password [Generate a Token from docker Hub and use it ]

Add as secret: 
Name:   KUBECONFIG_DATA 
Secret :  

To get Kubernetes Config and secret check it from controle plan 
You CANNOT directly paste this YAML into a secret variable 
Run this:   cat ~/.kube/config | base64 -w 0 


## GitHub Actions Workflow 

## test it 
 Commit & Push 
git add . 
git commit -m "added github actions" 
git push origin main 


 
 
