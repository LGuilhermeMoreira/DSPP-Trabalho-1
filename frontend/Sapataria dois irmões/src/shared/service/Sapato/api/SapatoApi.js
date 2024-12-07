import { api } from "../../api/axios";

class SapatoAPI {
    async Root(){
        try {
            const response = await api.get('/')
            return response
        } catch (error) {
            console.log(error)
            return error
        }
    }
}

export default new SapatoAPI()