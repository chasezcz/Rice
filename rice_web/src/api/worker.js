import request from '@/utils/request'

export function getAllWorkers() {
  return request({
    url: '/worker/all',
    method: 'get'
  })
}

export function addWorker(data) {
  return request({
    url: 'worker/add',
    method: 'get',
    data
  })
}

export function updateWorker(data) {
  return request({
    url: 'worker/update',
    method: 'get',
    data
  })
}
