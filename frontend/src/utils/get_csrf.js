const get_csrf = () => {
    return document.getElementsByTagName('meta')['csrf-token'].getAttribute('content')
}

export default get_csrf