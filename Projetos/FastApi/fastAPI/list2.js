export default function ListProduct(props, res) {

    const data = []
    let authToken = null

    // res.status(200).json({ text: 'Hello' })
    /**
     * endpoint(homologação): https://api.catalogo-yandeh.a.visie.link
     * resource(via props): props.content = Ex: produto, usuário
     * 
     * endpoint(keylock): https://sso-dev.yandeh.com.br/auth/realms/YandehQA/protocol/openid-connect/token
    */

    console.log(props)
    /**
    async function getToken(){
         await let token = fecth(endpoint(keylock), 
           { header: 
               { 'Content-Type': 'multipart/form-data' }, 
           method: POST, body: {...Campos Form data} }
          ).then(response => response.json())
           .then(data => authToken = data.access_token)
           .catch(error => console.log(error))
            
        return token
    }
*/
    function openModal(){
        console.log('Cliquei em algum PRONTO pra MODAL!')
    }

    function opAdd(){
        fetch(`https://api.catalogo-yandeh.a.visie.link/products`, { headers: {'Authorization': authToken }, method: POST, body: {getoken} }) 
        console.log('Adiciona Item')
    }

    function opUpdate(){
        fetch(`https://api.catalogo-yandeh.a.visie.link/product`, { headers: {'Authorization': authToken }, method: PUT, body: {getoken} }) 
        console.log('Update Item')
    }

    function opDelete(){
        fetch(`https://api.catalogo-yandeh.a.visie.link/product/${props.content}`, { headers: {'Authorization': authToken }, method: DELETE, body: {getoken} }) 
        console.log('Delete Item')
    }

    function listData(){
        // CREATE - READ
        const authToken = getToken()
        fetch(`https://api.catalogo-yandeh.a.visie.link/product/${props.content}`, { headers: {'Authorization': authToken }, method: GET, body: {getoken} })
        
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