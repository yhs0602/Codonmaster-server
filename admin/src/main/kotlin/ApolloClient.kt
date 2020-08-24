//import kotlin.js.Promise
//
//external enum class NetworkStatus {
//
//}
//
//external class ApolloError{
//    val message: String
//    val graphQLErrors: Array<GraphQLError>
//    val networkError: Error?
//    val extraInfo: Any
//}
//
//external class ApolloQueryResult<TData, TVariables>{
//    val data: TData
//    val loading: Boolean
//    val error: ApolloError
//    val variables : Map<String, Any>
//    val networkStatus: NetworkStatus
//    fun refetch(variables: Partial<TVariables>) : Promise<ApolloQueryResult>
//
//    fun fetchMore(): Promise<ApolloQueryResult>
//    fun startPolling(interval: Number): Unit
//    fun stopPolling(): Unit
//    fun subscribeToMore(options: Array<>)
//    fun updateQuery(previousResult: TData, options: Array<TVariables>): TData
//    val client: ApolloClient
//    val called: Boolean
//}
//
//external class ApolloClient(uri: String, cache: InMemoryCache) {
//    fun query(query: String): Promise<ApolloQueryResult>
//}
//
//external class InMemoryCache {
//
//}