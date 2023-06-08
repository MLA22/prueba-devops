pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo "Flask\npytest" > requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh '''\
                    echo "def test_devops_endpoint(client):
                        response = client.post(
                            '/DevOps',
                            headers={'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'},
                            json={
                                'message': 'This is a test',
                                'to': 'Juan Perez',
                                'from': 'Rita Asturia',
                                'timeToLifeSec': 45
                            }
                        )
                        assert response.status_code == 200
                        assert response.json == {'message': 'Hello Juan Perez your message will be sent'}
                    " > test_app.py'''
                sh 'pytest test_app.py'
            }
        }
        
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                // Add the deployment steps for the production environment here
            }
        }
    }
}
