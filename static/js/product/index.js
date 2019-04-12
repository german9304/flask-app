// import Review from './modules/review';
import { ProductsAPI, ProductAPI } from './modules/products';


const url = new URL(document.location); // url

console.log(url.searchParams.get('id'));

ProductsAPI('/api/products')
  .then(data => console.log(data));

const productId = url.searchParams.get('id');
ProductAPI(`/api/product/${productId}`)
  .then(({ data }) => console.log(data.reviews_assoc));
