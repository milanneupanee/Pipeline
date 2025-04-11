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