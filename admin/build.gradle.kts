plugins {
    kotlin("js") version "1.4.0"
    id("com.apollographql.apollo").version("2.3.0")
}
group = "com.kyhsgeekcode"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    jcenter()
    maven {
        url = uri("https://dl.bintray.com/kotlin/kotlinx")
    }
    maven {
        url = uri("https://dl.bintray.com/kotlin/kotlin-js-wrappers")
    }
}
dependencies {
    testImplementation(kotlin("test-js"))
    implementation("org.jetbrains.kotlinx:kotlinx-html-js:0.7.2")
    implementation("org.jetbrains:kotlin-react:16.13.1-pre.110-kotlin-1.4.0")
    implementation("org.jetbrains:kotlin-react-dom:16.13.1-pre.110-kotlin-1.4.0")
    implementation("org.jetbrains:kotlin-styled:1.0.0-pre.110-kotlin-1.4.0")
    implementation(npm("@apollo/client", "3.1.3"))
    implementation(npm("graphql", "15.3.0"))
    // The core runtime dependencies
//    implementation("com.apollographql.apollo:apollo-runtime:2.3.0")
    // Coroutines extensions for easier asynchronicity handling
//    implementation("com.apollographql.apollo:apollo-coroutines-support:2.3.0")

}
kotlin {
    js {
        browser {
            binaries.executable()
            webpackTask {
                cssSupport.enabled = true
            }
            runTask {
                cssSupport.enabled = true
            }
            testTask {
                useKarma {
                    useChromeHeadless()
                    webpackConfig.cssSupport.enabled = true
                }
            }
        }
//        binaries.executable()
    }
}

apollo {
    // instruct the compiler to generate Kotlin models
    generateKotlinModels.set(true)
}

// Heroku Deployment (chapter 9)
tasks.register("stage") {
    dependsOn("build")
}

