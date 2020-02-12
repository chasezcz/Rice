<template>
  <div style="padding: 10px 20px 0 20px">
    <div style="padding: 0 0 20px 0">
      <h1>产品种类数量：{{ list.length }}</h1>
      <el-button type="primary" @click="dialogVisible = true">添加新产品</el-button>
    </div>
    <el-table :data="list" border fit highlight-current-row class="productTable">
      <el-table-column align="center" label="序号">
        <template slot-scope="{row, $index}">
          <span>{{ $index + 1 }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="名称">
        <template slot-scope="{row}">
          <span>{{ row.label }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="最后一次进货时间">
        <template slot-scope="{row}">
          <!-- <span>{{ row.last_supple_date | parseTime('{y}-{m}-{d} {h}:{i}') }}</span> -->
          <span>{{ row.last_supple_date | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>

      <el-table-column label="持有数量(/箱)">
        <template slot-scope="{row}">
          <span>{{ row.owned_number }}</span>
        </template>
      </el-table-column>

      <el-table-column label="标准价(/人民币)">
        <template slot-scope="{row}">
          <span>{{ row.stardand_price }}</span>
        </template>
      </el-table-column>

      <el-table-column label="状态">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter">
            {{ row.status | statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="操作">
        <template slot-scope="{row}">
          <el-button
            type="success"
            icon="el-icon-circle-check-outline"
            @click="confirmEdit(row)"
          >
            修改
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      title="操作"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <div>
        <el-form ref="productData" :model="productData" label-width="100px">
          <el-form-item label="产品名称" required>
            <el-input v-model="productData.label" />
          </el-form-item>
          <el-form-item label="标准售价">
            <el-input v-model="productData.stardand_price" />
          </el-form-item>
          <el-form-item label="持有数量">
            <el-input v-model="productData.owned_number" />
          </el-form-item>
          <el-form-item label="最后一次进货" required>
            <el-date-picker v-model="productData.last_supple_date" type="date" placeholder="选择日期" style="width: 100%;" />
          </el-form-item>
          <el-radio-group v-model="productData.status">
            <el-radio label="ON_SALE">销售中</el-radio>
            <el-radio label="OFF_SALE">停售</el-radio>
            <el-radio label="EXHAUST">缺货</el-radio>
          </el-radio-group>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleCreate">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getAllProducts, addProduct } from '@/api/product'
export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'ON_SALE',
        draft: 'OFF_SALE',
        deleted: 'EXHAUST'
      }
      return statusMap[status]
    },
    statusFilter2(status) {
      const statusMap = {
        'ON_SALE': '销售中',
        'OFF_SALE': '停售',
        'EXHAUST': '缺货'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: [],
      dialogVisible: false,
      productData: {}
    }
  },
  created: function() {
    getAllProducts().then(response => {
      this.list = response.data
    })
  },
  methods: {
    handleCreate() {
      addProduct(this.productData).then(response => {
        if (response.code === 20000) {
          this.$message({
            message: '操作成功',
            type: 'success'
          })
        } else {
          this.$message({
            message: '操作失败' + response.detail,
            type: 'warning'
          })
        }
      })
    },
    confirmEdit(row) {
      this.productData = row
      this.dialogVisible = true
    },
    handleClose() {
      this.productData = {}
      this.dialogVisible = false
    }
  }
}
</script>

<style lang="scss" scoped>
.productTable {
  margin: 0 auto;
  padding: 0 20px 0 20px;
}
</style>
