import request from '@/utils/request'

export function getAllProducts() {
  return request({
    url: '/product/all',
    method: 'get'
  })
}

export function addProduct(data) {
  return request({
      url: 'product/add',
      method: 'POST',
      data
  })
}

export function updateProduct(data) {
  return request({
    url: 'product/update',
    method: 'POST',
    data
  })
}
