import { get } from '../api/api';


async function FetchUser() {
  return get('/api/user');
}


export default FetchUser;
