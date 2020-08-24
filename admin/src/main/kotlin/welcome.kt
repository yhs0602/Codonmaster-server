import kotlinx.html.InputType
import kotlinx.html.js.onChangeFunction
import org.w3c.dom.HTMLInputElement
import org.w3c.xhr.XMLHttpRequest
import react.RBuilder
import react.RComponent
import react.RProps
import react.RState
import styled.css
import styled.styledDiv
import styled.styledInput
import kotlin.js.Json
import kotlin.js.json

external interface WelcomeProps : RProps {
    var name: String
}

data class WelcomeState(val name: String) : RState

@JsExport
class Welcome(props: WelcomeProps) : RComponent<WelcomeProps, WelcomeState>(props) {

    init {
        state = WelcomeState(props.name)
    }

    override fun RBuilder.render() {
        styledDiv {
            css {
                +WelcomeStyles.textContainer
            }
            +"Hello, ${state.name}"
        }
        styledInput {
            css {
                +WelcomeStyles.textInput
            }
            attrs {
                type = InputType.text
                value = state.name
                onChangeFunction = { event ->
                    setState(
                        WelcomeState(name = (event.target as HTMLInputElement).value)
                    )
                }
            }
        }
        styledInput {
            css {
                +WelcomeStyles.roundToggle
            }
            attrs {
                type = InputType.checkBox
                onChangeFunction = { event ->
                    console.log("Switched")
                    val request = XMLHttpRequest()
//                    request.open("POST", "https://fierce-beyond-62887.herokuapp.com/graphql", true)
                    request.open("POST", "http://127.0.0.1:8000/graphql", true)
                    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                    request.onload = {
                        val response = JSON.parse<Json>(request.responseText)
                        val data = response["data"] as Json
                        val array = data["announcements"]
//                        console.log(array)
                        for (a in array.asDynamic()) {
                            val announcementData = a as Json
                            console.log(announcementData["title"])
                        }
                        setState(
                            WelcomeState(name = "${request.status} ${request.responseText}")
                        )
                    }
//                    val map = HashMap<String, Any>()
//                    map["query"] = "query{announcement{title}}"
//                    map["operationName"] = ""
//                    map["variables"] = HashMap<String, String>()

                    val content = JSON.stringify(
                        json(
                            "query" to "query{announcements{title}}",
                            "operationName" to "",
                            "variables" to "{}"
                        )
                    )
//                    JSON.stringify(map)

                    console.log(content)
                    request.send(content)
                    console.log("Sent")
                }
            }
        }
    }
}
