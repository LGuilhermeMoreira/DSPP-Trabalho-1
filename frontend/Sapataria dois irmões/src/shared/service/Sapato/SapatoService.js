import SapatoApi from "./api/SapatoApi";

class SapatoService{
    async test(){
       const response = await  SapatoApi.Root()
       console.log(response)
    }
}

export default new SapatoService()  

