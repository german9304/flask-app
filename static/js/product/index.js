// import Review from './modules/review';
import { ProductsAPI, ProductAPI } from './modules/products';
import createReviewElements from './modules/review';
import spinner from './modules/spinner';

const url = new URL(document.location); // url
const productReviews = document.getElementById('product-reviews');

productReviews.appendChild(spinner);

console.log(url.searchParams.get('id'));

ProductsAPI('/api/products')
  .then(data => console.log(data));

const productId = url.searchParams.get('id');


ProductAPI(`/api/product/${productId}`)
  .then(({ data }) => {
    const fragment = document.createDocumentFragment();
    const reviews = createReviewElements(data.reviews_assoc);
    reviews.forEach(review => fragment.appendChild(review));
    // console.log(reviews);
    spinner.remove();
    productReviews.appendChild(fragment);
  });
