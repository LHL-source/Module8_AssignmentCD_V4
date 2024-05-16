In de READ.md is te lezen de volgende onderdelen:
Assignment cd 2 opdrachten :
Voor de assignment CD zijn volgende 2 opdrachten die hieronder worden uitgewerkt:
1)Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.
2)Discuss three problems that you encountered along the way and how you solved them.

3)beschijving van het project Assignment CD welk onderdeel is als 1 van de eind opdrachten van de backend opleiding.

ad 1) 3 componenten:
Component:1)in local machine is er een map aangemaakt met naam Assign_cd. Op local machine wordt via VS code volgende files geplaatst in map Assign_cd:
1.1)GitHub workflows map met daarin yml_file:runt_tests_and_deploy.yml
1.2)in map Assign_CD de volgende files:
1.2.1)lib.py: hierin staat de flask app
1.2.2)test_lib.py:hierin staat de test file voor lib.py
1.2.3)requirements.txt: de dependencies
1.2.4)READ.md:antwoorden op de vragen van assignment CD van de tutorial

Component:2)git,Github en GitHub actions:
Via de cmd wordt de componenten van 1 via git ingelezen. De rede van gebruik van git is vanwege versie bijhouden en mogelijk maken voor "collaboration" (samenwerking) met developers van andere discipline b.v. testing. Via git wordt de gegevens van component 1 welk de locatie  de local machine heeft, doorgezet naar GitHub .De rede hiervan is in GitHub is het component GitHub Actions die de workflow opgang zet.

Component:3) workflow en server:1 van de taken die in de workflow is gedefinieerd is de flaks app testen en doorzetten naar de server (vps, droplet van digitalocean) zodat de flask app in de web browser komt en de gebruikers dit kan gebruiken. De tool die dit deze taak krijgt is de vps . 

2)Discuss three problems that you encountered along the way and how you solved them.

2.1) Git master, main:Tijdens het push van git naar GitHub is geconstateerd dat de default branch bij git master is en bij GitHub main. Door de default branch van git te wijzigen naar main branch is dit probleem opgelost.
2.2) Inzichtelijk maken de errors d.m.v. debug step in workflow welke zichtbaar wordt in GitHub Actions:b.v.
codes: pwd  # Print current directory
       ls   # List files in the current directory
Het gevolg hiervan is dat inzichtelijk wordt gemaakt wat de error is kan de developer gerichter zoeken naar een oplossing wat tijd (en geld) bespaard.
2.3)Begrijpen wat het concept is van CI/CD:inzichtelijk maken van het concept: door elk component te bestuderen met vragen als wat is dit voor iets, wat is de functie er van, welk plaats neemt die component in het proces, hoe is de relaties van dit component met de voorafgaande en volgende component. Daarnaast inzichtelijke maken d.m.v. analogie hoe het process in elkaar zit. Door de kennis hiervan heb je beter inzicht in wat je doet en begrijp je hoe en waarom de volgorde. Ten gevolge hiervan kan je gerichter zoeken naar antwoorden op fouten (errors) die tijdens het proces ontstaat. Aangezien dit een complexe opdracht is, is kans op fouten (errors) groter en vanwege de gelaagdheid is het lastig de fouten op te sporen. Om dit probleem te mininaliseren worden de componenten (en ook andere elementen) voordat de component in de workflow wordt geplaatst geisoleerd getest. Dit zorgt er voor dat de flask app de volgende kwaliteit heeft: robuustheid, betrouwbaarheid en consistentie . Uiteraard heeft de CI/CD ook een grote bijdrage van de genoemde kwaliteiten. 

Ter completering van het project Assignment CD welk een onderdeel is als 1 van de laaste opdracht van de backened opleiding van Winc Academy is hieronder een beschrijving van de opdracht:

Assignment: CD
You need to master the following to complete this assignment:

Creating and provisioning a server at Digital Ocean;
Connecting to a Linux server over SSH;
Running basic terminal commands on a Linux server;
Deploying a Flask application on a Linux server.
Continuous Deployment (CD) is the idea of having the product your team is working on be deployed frequently, where 'deployed' means packaged and distributed to the customer(s). For the web, this mostly means updating some code. It is not set in stone how frequent deployment should happen before it's 'continuous'. Some teams work with nightlies (nightly releases) and other teams deploy several times a day.

In this assignment you will use GitHub Actions to implement a continuous deployment pipeline. As a starting point, we assume you have set up a VPS running a Flask application as described in a previous exercise. If this is not the case, go back to those instructions and set one up.

The continous deployment pipeline should look like this:

You manually write, commit and push some code. This only requires you to be familiar with git.
GitHub Actions runs tests on your code. You can use Pytest for this.
If and only if the tests pass, GitHub Actions logs into the VPS you have running with Digital Ocean and runs commands such that the code is updated to the latest version.
The only new part here is step 3, and we will let you think about how to best implement this. Here are some tips that you might find useful:

Tip 1: GitHub: Deploy Keys(opens in a new tab)

You can think of an SSH key as a username and password in one. You can use it to make reading and writing to repositories under your account on GitHub easier. A deploy key is an SSH key that grants access to just one repository. You can even set the key to only allow read-only access for extra security.

Tip 2: sh files.** You should be fairly comfortable with the Bash by now. For this assignment it would come in handy if you were able to chain Bash commands! This can be done by placing commands you want to run in a .sh file and running it with sh example.sh. It's just like programming in any other language!

echo "Here is some code."
echo "We wrote it in Bash."
echo "Bash is just a programming language, really."
# This is a comment.
# Let's read a file.
cat some_file.txt
# Do something extremely useful for continous deployment
git pull
# Hmmm, we should probably restart the application after we've pulled in
# new code, otherwise we can be looking for what went wrong for quite a
# while..
systemctl restart my-application
# Verify the application is running
systemctl status my-application
Tip 3: Secrets. In order to execute commands on the VPS that your application is running on you need to have access to it within a workflow on GitHub Actions. On the other hand we don't never want to put log-in credentials in the repository itself. The way to do this is by using encrypted secrets.

GitHub Actions -- Creating Encrypted Secrets for a Repository(opens in a new tab)
GitHub Actions -- Using Encrypted Secrets in a Workflow(opens in a new tab)
💡 Note

It's usually not a good idea to give continuous deployment pipelines root access to your server, but we will accept it for this assignment. If you are interested, you can look into how to create and use new users on Ubuntu (and Linux in general).

It's up to you to put the pieces of the puzzle together and create the continuous deployment pipeline as described above. The complexity of your Flask application is not important here, only that you use a GitHub Actions workflow to test and -- if it passed -- update the code running on your server after a push.

Finally, write a short, 200/300-word report in which you discuss at least the following:

Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.
Discuss three problems that you encountered along the way and how you solved them.
(optional) Anything of note that you want to share about the process of solving this assignment.
You can include this report as a README.md file in your repository. You can use Markdown syntax to structure your document if you want, but it is not required.



