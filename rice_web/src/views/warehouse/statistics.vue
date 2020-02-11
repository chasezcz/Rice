<template>
  <div>
    <el-collapse accordion="true">
      <el-collapse-item class="s-collapse-item" title="按送货员统计">
        <el-collapse>
          <el-collapse-item v-for="(worker, index) in statisticsByWorker" :key="index" class="s-collapse-item" :title="worker.name">
            <el-table border fit highlight-current-row :data="worker.products" style="font-size:20px">
              <el-table-column label="货品" prop="label">
                <template slot-scope="{row}">
                  {{ row.label }}
                </template>
              </el-table-column>
              <el-table-column label="出货量" prop="number">
                <template slot-scope="{row}">
                  {{ row.number }}
                </template>
              </el-table-column>
            </el-table>
          </el-collapse-item>
        </el-collapse>
      </el-collapse-item>
      <el-collapse-item class="s-collapse-item" title="按商品统计">
        <el-collapse>
          <el-collapse-item v-for="(product, index) in statisticsByProduct" :key="index" class="s-collapse-item" :title="product.name">
            <el-table border fit highlight-current-row :data="product.worker" style="font-size:20px">
              <el-table-column label="送货员" prop="name">
                <template slot-scope="{row}">
                  {{ row.name }}
                </template>
              </el-table-column>
              <el-table-column label="出货量" prop="number">
                <template slot-scope="{row}">
                  {{ row.number }}
                </template>
              </el-table-column>
            </el-table>
          </el-collapse-item>
        </el-collapse>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import { statisticsToday } from '@/api/warehouse'
export default {
  data() {
    return {
      statisticsByWorker: this.statisticsByWorker,
      statisticsByProduct: this.statisticsByProduct
    }
  },
  created: function() {
    statisticsToday().then(response => {
      this.statisticsByWorker = response.data['statisticsByWorker']
      this.statisticsByProduct = response.data['statisticsByProduct']
    }).catch(_ => {
      this.statisticsByWorker = []
      this.statisticsByProduct = []
    })
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
.s-collapse-item >>> .el-collapse-item__header {
  padding-left: 10px;
  font-size: 25px;
}
</style>
