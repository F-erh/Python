export default function ListProduct(props) {

    const data = []
    let authToken = null


    /**
     * Lógica inicial para testar integração com backend
     * endpoint(homologação): https://api.catalogo-yandeh.a.visie.link
     * resource(via props): props.content = Ex: produto, usuário
     * 
     * endpoint(keylock): https://sso-dev.yandeh.com.br/auth/realms/YandehQA/protocol/openid-connect/token
    */

    console.log(props)

    async function getToken(){
        /**
         * await let token = fecth(endpoint(keylock), 
         *  { header: 
         *      { 'Content-Type': 'multipart/form-data' }, 
         *  method: POST, body: {...Campos Form data} }
         * ).then(response => response.json())
         *  .then(data => authToken = data.access_token)
         *  .catch(error => console.log(error))
         */ 
        
        //return token
    }

    function openModal(){
        console.log('Cliquei em algum PRONTO pra MODAL!')
    }

    function opAdd(){
        // fecth(/endpoint/, { header: {...}, method: POST, body: {...} }) // CREATE - CRUD
        console.log('Adiciona Item')
    }

    function opUpdate(){
        // fecth(/endpoint/, { header: {...}, method: PUT, body: {...} }) // CREATE - UPDATE
        console.log('Update Item')
    }

    function opDelete(){
        // fecth(/endpoint/, { header: {...}, method: DELETE, body: {...} }) // CREATE - DELETE
        console.log('Delete Item')
    }

    function listData(){
        // CREATE - READ
        /**
         * fecth(/`${endpoint}/${resource}`/, { header: {...}, method: GET, body: {... token} }) // CREATE - READ
         */

        const authToken = getToken()
        fetch(`https://api.catalogo-yandeh.a.visie.link/${props.content}`, { headers: {'Authorization': authToken } })
        
        console.log('Lista data')
    }

    
    
    return (
        <>
            <div><span onClick={opAdd}>Adicionar</span></div>
            <ul>
                <li onClick={openModal}>Item A <span k={opUpdate}>atualizar</span><span onClick={opDelete}>d ar</span></li>
                <li onClick={openModal}>Item B <span onClick={opUpdate}>atualizar</span><span onClick={opDelete}>deletar</span></li>
                <li onClick={openModal}>Item C <span onClick={opUpdate}>atualizar</span><span onClick={opDelete}>deletar</span></li>
                <li onClick={openModal}>Item D <span onClick={opUpdate}>atualizar</span><span onClick={opDelete}>deletar</span></li>
                <li onClick={openModal}>Item E <span onClick={opUpdate}>atualizar</span><span onClick={opDelete}>deletar</span></li>
            </ul>
        </>
    )
}