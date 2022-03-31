
export default class update {

    static DeleteComment(props) {
        return fetch(`http://172.29.128.254:8080/deleterates/`, {
            'methods': 'POST',
            headers: {
                'Content-Type': 'applications/json'
            }

        }
    ,)
    }
}
