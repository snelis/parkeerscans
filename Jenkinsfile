#!groovy

def tryStep(String message, Closure block, Closure tearDown = null) {
    try {
        block();
    }
    catch (Throwable t) {
        slackSend message: "${env.JOB_NAME}: ${message} failure ${env.BUILD_URL}", channel: '#ci-channel', color: 'danger'

        throw t;
    }
    finally {
        if (tearDown) {
            tearDown();
        }
    }
}


node {

    stage("Checkout") {
        checkout scm
    }

    stage("Build develop kibana") {
        tryStep "build", {
            def image = docker.build("build.datapunt.amsterdam.nl:5000/datapunt/predictive_parking_kibana:${env.BUILD_NUMBER}", "kibana")
            image.push()
            image.push("acceptance")
        }
    }



    stage("Build develop logstash") {
        tryStep "build", {
            def image = docker.build("build.datapunt.amsterdam.nl:5000/datapunt/predictive_parking_logstash:${env.BUILD_NUMBER}", "logstash")
            image.push()
            image.push("acceptance")
        }
    }

    stage("Build develop csvimporter") {
        tryStep "build", {
            def image = docker.build("build.datapunt.amsterdam.nl:5000/datapunt/predictive_parking_csvpgvoer:${env.BUILD_NUMBER}", "csvimporter")
            image.push()
            image.push("acceptance")
        }
    }

    stage("Build develop web/python") {
            tryStep "build", {
                def image = docker.build("build.datapunt.amsterdam.nl:5000/datapunt/predictive_parking:${env.BUILD_NUMBER}", "web")
                image.push()
                image.push("acceptance")
            }
    }

    //TODO tests!!
}