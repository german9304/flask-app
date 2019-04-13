// import Review from './modules/review';
import { fetchProducts, fetchProduct } from './modules/products';
import FetchUser from './modules/user';
import {
  createReviewElements,
  createReview,
  createReviewAPI,
  createReviewElement,
} from './modules/review';
import spinner from './modules/spinner';


let state = {
  product: {},
  user: {},
};

const url = new URL(document.location); // url
const productReviews = document.getElementById('product-reviews');
const formReviewComments = document.getElementById('form-review__comments');

productReviews.appendChild(spinner);

fetchProducts('/api/products')
  .then(data => console.log(data));

const productId = url.searchParams.get('id');


fetchProduct(`/api/product/${productId}`)
  .then(({ data }) => {
    state = { ...state, product: data };
    const fragment = document.createDocumentFragment();
    const reviews = createReviewElements(data.reviews_assoc);
    reviews.forEach(review => fragment.appendChild(review));
    spinner.remove();
    productReviews.appendChild(fragment);
  });

FetchUser()
  .then(({ data }) => {
    state = { ...state, user: data };
  })
  .catch(() => {

  });

function handleAddReview(e) {
  e.preventDefault();
  const { product } = state;
  const formData = new FormData(formReviewComments);
  const review = createReview(formData.get('comment'), product.id);
  const reviewApi = createReviewAPI(review);
  reviewApi
    .then(({ data }) => {
      const createdReview = createReviewElement(data);
      productReviews.appendChild(createdReview);
    })
    .catch(() => console.log('error'));
}


formReviewComments.addEventListener('submit', handleAddReview);
