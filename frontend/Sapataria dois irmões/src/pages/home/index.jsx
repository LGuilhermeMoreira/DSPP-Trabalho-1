import { Container, ContentBody, ContentBorder, ContentButtons, HeaderName, MessageStatus } from "./styles"

export const Home = () => {
    return <>
        <Container>
            <HeaderName>
                <h1>Sapataria dois irmões</h1>
            </HeaderName>
            <ContentBody>
                <ContentBorder>
                    <p>Listagem dos sapatos</p>
                </ContentBorder>
                <ContentButtons>
                    <button>Download CSV</button>
                    <button>Gerar Hash</button>
                    <button>Adicionar Sapato</button>
                </ContentButtons>
            </ContentBody>
            <MessageStatus>
                <h1>msg:</h1>
            </MessageStatus>
        </Container>
    </>
}