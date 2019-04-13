
import { get, post } from '../api/api';
/**
 *
 * fetches products from api
 */
async function fetchProducts(url) {
  const data = get(url);
  return data;
}

async function createProductAPI(url, options) {
  const data = post(url, options);
  return data;
}

async function fetchProduct(url) {
  const data = get(url);
  return data;
}


export {
  fetchProducts, createProductAPI, fetchProduct,
};
