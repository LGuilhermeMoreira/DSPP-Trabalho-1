import styled from "styled-components";

export const Container = styled.div`
    background-color: #CECED2;
    height: 100dvh;
    display: flex;
    flex-direction: column;
    padding: 2rem;
    gap: 1rem;
`
export const HeaderName = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
`
export const ContentBody = styled.div`
    flex: 1;
    display: flex;
    gap: 5rem;
`

export const ContentBorder = styled.div`
    display: flex;
    flex-direction: column;
    border: 1px solid black;
    padding: 1rem;
    border-radius: 1rem;
    background-color: white;
    width: 100%;
`

export const ContentButtons = styled.div`
    display: flex;
    flex-direction: column;
    gap: 1rem;
`

export const MessageStatus = styled.div`
    display: flex;
`
