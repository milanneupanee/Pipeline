pipeline{
    agent any
    tools{
        maven "MAVEN3" //same name as provided in jenkins
        jdk "OrackeJDK8"
    }

    stages{
        stage('Fetch code'){
            steps{
                git branch: 'vp-rem', url: 'https://github.com/devopshydclub/vprofile-repo.git'

            }
        }

        stage('Build'){
            steps{
                sh 'mvn install -DskipTEsts'
            }
            post{
                success{
                    echo 'Now archiving it ...'
                    archiveArtifacts: '**/target/*.war'
                }
            }
        }
        
        stage('Unit test'){
            steps{
                sh 'mvn test'
                 //we can check pipeline till here too
            }
        }
        stage('Checkstyle Analysis'){
            steps{
                sh 'mvn checkstyle:checkstyle'
                //we can check pipeline till here too
            }
        }
        //Now we try to scan code with sonarqube
        //maven is using the sonarqube
        //do some research for this topic
        stage('Soanr analysis'){
            environment{
                scannerHome= tool 'sonar4.7'
            }
        }
        steps {
            withSonarQubeEnv('sonar'){//sonar is name set in the jenkins
                sh '''${scannerHome}/bin/sonar-scaner -Dsonar.projectKey=vprofile \
                -Dsonar.projectName = vprofile-repo \
                -Dsonar.projectVersions=1.0 \
                -Dsonar.sources=src/ \ 
                -Dsonar.java.binaries=target/test-classes/com/visualpathit/account/controllerTest/ \
                -Dosnar.junit.reportsPath=target/surefire-reports/ \
                -Dsoanr.jacoco.reportsPath=target/jacoco.exec \
                -Dsonar.java.checkstyle.reportPaths=target/checkstyle-result.xml
                '''
            }//taken from documentations
            //Now build it in the jenkins by following the following steps
        }
        //Now for the quality gates
        stage("Quality gates"){
            steps{
                timeout(time: 1, unit: 'HOURS'){
                    //Parameter indicates whether to set pipeline to UNSTABLE if quality gate the fails
                    //true =set pipeline to UNSTABLE false =dont
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        /*setup sonarqube server
       1 goto sonarque page
       2 goto quality gate
       3 create quality gate
       4 add condition
       5 add bug matrix if bug more than 60  fail it
       
       It send notifications to jenkins via webhooks For that we need to set it
       1 go to project settings
       2 create webhooks
       3 give name
       4 in url jenkinsurl/sonarqube-webhook
       5 create

       copy and build it again
       it will show the info about it 
        */


        /* Now  adding nexus to the jenkins
        1 research for that (nexus artifact uploader)
        2 read documentation
        */
        stage("Upload artifact"){
            steps{
                 nexusArtifactUploader(
                    nexusVersion: 'nexus3',
                    protocol: 'http',
                    nexusUrl: 'my.nexus.address',
                    groupId: 'com.example',
                    version: "${env.BUILD_ID}-${env.BUILD_TIMESTAMP}",
                    repository: 'vprofile-repo',
                    credentialsId: 'CredentialsId',
                    artifacts: [
                        [artifactId: 'vproapp',
                        classifier: '',
                        file: 'target/vprofile-v2.war',
                        type: 'war']
                    ]
                )//adjust the value as per requirment
                //run it 

            }
        }
    }
}
/* to run this pipeline
1 Go to jenkins
2 create new item
3 give name
4 select pipeline
5 write scripts or select the code
6 save

and finally build it
*/