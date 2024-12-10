import { useState } from "react";
import { Container, ContentBody, ContentBorder, ContentButtons, HeaderName, MessageStatus } from "./styles"
import { Button, Modal, Space, Table } from "antd";

export const Home = () => {
    
  const [modal2Open, setModal2Open] = useState(false);


    const dataSource = [
        {
          key: '1',
          tamanho: 32,
          marca: 'Puma',
          modelo: "Puma Pantera cor de rosa",
          cor: 'vermelho',
        },
        {
          key: '2',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '3',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '4',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '5',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '6',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '7',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '8',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '9',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '10',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '11',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '12',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '13',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
        {
          key: '14',
          tamanho: 40,
          marca: 'Nike',
          modelo: "Nike Nvidea full definition",
          cor: 'branco',
        },
      ];
      
      const columns = [
        {
          title: 'Marca',
          dataIndex: 'marca',
          key: 'marca',
        },
        {
          title: 'Modelo',
          dataIndex: 'modelo',
          key: 'modelo',
        },
        {
          title: 'Tamanho',
          dataIndex: 'tamanho',
          key: 'tamanho',
        },
        {
          title: 'Cor',
          dataIndex: 'cor',
          key: 'cor',
        }, 
        {
          title: 'Ações',
          key: 'acoes',
          render: () => (
            <Space size="middle">
              <a>Editar </a>
              <a>Deletar</a>
            </Space>
          ),
        }
      ];
      
      
      return <>
        <Container>
            <HeaderName>
                <h1>Sapataria dois irmões</h1>
            </HeaderName>
            <ContentBody>
                <ContentBorder>
                    <Table dataSource={dataSource} columns={columns} pagination={{pageSize: 6}} />
                </ContentBorder>
                <ContentButtons>
                    <Button type="primary">Download CSV</Button>
                    <Button type="primary">Gerar Hash</Button>
                    <Button type="primary" onClick={() => setModal2Open(true)}>Adicionar Sapato</Button>
                </ContentButtons>
            </ContentBody>
            <MessageStatus>
                <h1>Msg Output:</h1>
                <p>Cód: 200 - Success Created</p>
            </MessageStatus>
        </Container>

        <Modal
            title="Adicionar Sapato"
            centered
            open={modal2Open}
            onOk={() => setModal2Open(false)}
            onCancel={() => setModal2Open(false)}
        >
            <p>teste</p>
        </Modal>
    </>
}