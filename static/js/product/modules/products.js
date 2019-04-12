
import { get, post } from '../api/api';
/**
 *
 * fetches products from api
 */
async function ProductsAPI(url) {
  const data = get(url);
  return data;
}

async function createProductAPI(url, options) {
  const data = post(url, options);
  return data;
}

async function ProductAPI(url) {
  const data = get(url);
  return data;
}


export {
  ProductsAPI, createProductAPI, ProductAPI,
};
