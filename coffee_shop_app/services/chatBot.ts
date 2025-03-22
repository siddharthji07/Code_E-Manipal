import axios from 'axios';
import { MessageInterface } from '@/types/types';
import { API_KEY, API_URL } from '@/config/runpodConfigs';

async function callChatBotAPI(messages: MessageInterface[]): Promise<MessageInterface> {
    try {
        // FastAPI endpoint for chat
        const endpoint = `${API_URL}/chat`;
        
        const response = await axios.post(endpoint, messages, {
            headers: {
                'Content-Type': 'application/json',
                ...(API_KEY && { 'Authorization': `Bearer ${API_KEY}` })
            }
        });
        
        // FastAPI returns the response directly
        return response.data;
    } catch (error) {
        console.error('Error calling the API:', error);
        throw error;
    }
}

export { callChatBotAPI };