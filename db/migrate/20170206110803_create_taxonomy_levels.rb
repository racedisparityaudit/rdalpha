class CreateTaxonomyLevels < ActiveRecord::Migration[5.0]
  def change
    create_table :taxonomy_levels do |t|
      t.string :level
      t.string :name
      t.string :parent_name
      t.integer :parent_id

      t.timestamps
    end
  end
end
